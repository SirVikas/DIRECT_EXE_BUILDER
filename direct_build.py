# direct_build.py - Direct PyInstaller Build (No PATH dependency)
"""
🚀 DIRECT PYINSTALLER BUILD
Uses PyInstaller module directly instead of command line
"""

import os
import sys
import PyInstaller.__main__
from datetime import datetime

def build_crm_exe_direct():
    """Build CRM EXE using PyInstaller module directly"""
    
    print("🚀 DIRECT CRM EXE BUILD")
    print("=" * 50)
    
    # Get current directory
    current_dir = os.getcwd()
    modules_dir = os.path.join(current_dir, 'modules')
    
    print(f"📁 Current directory: {current_dir}")
    print(f"📁 Modules directory: {modules_dir}")
    
    # Check essential files
    if not os.path.exists('main.py'):
        print("❌ main.py not found!")
        return False
    
    if not os.path.exists(modules_dir):
        print("❌ modules directory not found!")
        return False
    
    print("✅ Found required files")
    
    # Prepare PyInstaller arguments
    build_args = [
        'main.py',                                    # Main script
        '--onefile',                                  # Single executable
        '--windowed',                                 # No console window
        '--name=CRM_Active_Enhanced',                 # EXE name
        
        # Include modules folder
        f'--add-data={modules_dir}{os.pathsep}modules',
        
        # Hidden imports for all modules
        '--hidden-import=modules',
        '--hidden-import=modules.constants',
        '--hidden-import=modules.logger_config',
        '--hidden-import=modules.utils',
        '--hidden-import=modules.db_manager',
        '--hidden-import=modules.address_book_gui',
        '--hidden-import=modules.file_creator_gui',
        '--hidden-import=modules.file_search_gui',
        '--hidden-import=modules.settings_gui',
        '--hidden-import=modules.lotting_system_gui',
        '--hidden-import=modules.dialogs',
        '--hidden-import=modules.screenshot_monitor',
        '--hidden-import=modules.crm_display_scaling',
        '--hidden-import=modules.enhanced_beautiful_gui',
        '--hidden-import=modules.beautiful_styling',
        '--hidden-import=modules.enhanced_standardized_integration',
        '--hidden-import=modules.migration_tools_gui',
        '--hidden-import=modules.customizations',
        '--hidden-import=modules.standardized_directory',
        '--hidden-import=modules.standardized_naming',
        
        # Tkinter imports
        '--hidden-import=tkinter',
        '--hidden-import=tkinter.ttk',
        '--hidden-import=tkinter.filedialog',
        '--hidden-import=tkinter.messagebox',
        
        # Other dependencies
        '--hidden-import=sqlite3',
        '--hidden-import=json',
        '--hidden-import=datetime',
        '--hidden-import=random',
        '--hidden-import=re',
        '--hidden-import=platform',
        '--hidden-import=subprocess',
        '--hidden-import=tempfile',
        '--hidden-import=logging',
        '--hidden-import=traceback',
        '--hidden-import=os',
        '--hidden-import=sys',
        
        # Image libraries
        '--hidden-import=PIL',
        '--hidden-import=PIL.Image',
        
        # Windows specific
        '--hidden-import=win32clipboard',
        '--hidden-import=win32con',
        
        # Build options
        '--clean',                                    # Clean previous builds
        '--noconfirm',                               # No confirmation prompts
        '--distpath=dist',                           # Output directory
        '--workpath=build',                          # Work directory
    ]
    
    # Add icon if exists
    if os.path.exists('icon.ico'):
        build_args.append('--icon=icon.ico')
        print("✅ Found icon.ico - will be included")
    
    # Add data files if they exist
    data_files = [
        'address_book.db',
        'app_config.json', 
        'contact_folder_map.json',
        'lots_data.json'
    ]
    
    for data_file in data_files:
        if os.path.exists(data_file):
            build_args.append(f'--add-data={data_file}{os.pathsep}.')
            print(f"✅ Found {data_file} - will be included")
    
    print("\n🔨 Starting PyInstaller build...")
    print("📋 Build arguments:")
    for arg in build_args:
        print(f"   {arg}")
    
    try:
        # Use PyInstaller.__main__.run() directly
        print("\n⚡ Building executable...")
        PyInstaller.__main__.run(build_args)
        
        # Check if build was successful
        exe_path = os.path.join('dist', 'CRM_Active_Enhanced.exe')
        if os.path.exists(exe_path):
            exe_size = os.path.getsize(exe_path) / (1024*1024)  # MB
            print(f"\n🎉 BUILD SUCCESSFUL!")
            print("=" * 40)
            print(f"✅ Executable created: {exe_path}")
            print(f"📊 File size: {exe_size:.1f} MB")
            print(f"📅 Build completed: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
            return True
        else:
            print("\n❌ Build completed but EXE not found!")
            return False
            
    except Exception as e:
        print(f"\n💥 Build failed with error: {e}")
        print("📝 Full error details:")
        import traceback
        traceback.print_exc()
        return False

def clean_previous_builds():
    """Clean previous build artifacts"""
    print("\n🧹 Cleaning previous builds...")
    
    dirs_to_clean = ['build', 'dist']
    files_to_clean = ['*.spec']
    
    for dir_name in dirs_to_clean:
        if os.path.exists(dir_name):
            try:
                import shutil
                shutil.rmtree(dir_name)
                print(f"✅ Cleaned {dir_name}/")
            except Exception as e:
                print(f"⚠️ Could not clean {dir_name}: {e}")
    
    # Clean spec files
    import glob
    for spec_file in glob.glob('*.spec'):
        try:
            os.remove(spec_file)
            print(f"✅ Cleaned {spec_file}")
        except Exception as e:
            print(f"⚠️ Could not clean {spec_file}: {e}")

def test_exe():
    """Test the built executable"""
    exe_path = os.path.join('dist', 'CRM_Active_Enhanced.exe')
    
    if not os.path.exists(exe_path):
        print("❌ EXE not found for testing")
        return False
    
    print(f"\n🧪 Testing executable: {exe_path}")
    print("📋 You can test it manually by running:")
    print(f"   {exe_path}")
    print("\n⚠️ Note: First run might be slow as Windows extracts files")
    
    return True

def main():
    """Main build process"""
    print("🚀 CRM DIRECT EXE BUILD")
    print("=" * 60)
    
    # Check PyInstaller
    try:
        import PyInstaller
        print(f"✅ PyInstaller version: {PyInstaller.__version__}")
    except ImportError:
        print("❌ PyInstaller not installed!")
        print("Install with: pip install pyinstaller")
        return
    
    # Offer to clean previous builds
    clean_choice = input("\n🧹 Clean previous builds? (y/n): ").lower().strip()
    if clean_choice in ['y', 'yes']:
        clean_previous_builds()
    
    # Build
    print("\n🔨 Starting build process...")
    success = build_crm_exe_direct()
    
    if success:
        print("\n" + "="*60)
        print("🎉 BUILD COMPLETED SUCCESSFULLY!")
        print("="*60)
        test_exe()
        
        print("\n📋 NEXT STEPS:")
        print("1. Navigate to dist/ folder")
        print("2. Run CRM_Active_Enhanced.exe") 
        print("3. Verify all modules load correctly")
        print("4. Test core functionality")
        
        print("\n💡 DEPLOYMENT:")
        print("- Copy CRM_Active_Enhanced.exe to target computer")
        print("- Copy data files (address_book.db, etc.) if needed")
        print("- No Python installation required on target!")
        
    else:
        print("\n💥 BUILD FAILED!")
        print("Check the error messages above for details")
    
    input("\nPress Enter to exit...")

if __name__ == "__main__":
    main()