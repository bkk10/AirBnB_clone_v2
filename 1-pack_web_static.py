from fabric.api import local
from datetime import datetime
import os


def do_pack():
    """
    Generates a .tgz archive from the contents of the web_static folder.
    Archive will be stored in the versions folder.
    Returns the archive path if successful, None otherwise.
    """
    try:
        # Create versions directory if it doesn't exist
        if not os.path.isdir("versions"):
            os.mkdir("versions")

        # Format timestamp
        now = datetime.now()
        timestamp = now.strftime("%Y%m%d%H%M%S")

        # Archive name
        archive_name = f"versions/web_static_{timestamp}.tgz"

        # Compress folder
        print(f"Packing web_static to {archive_name}")
        result = local(f"tar -cvzf {archive_name} web_static", capture=True)

        # Check if file was created
        if os.path.exists(archive_name):
            print(f"web_static packed: {archive_name} -> {os.path.getsize(archive_name)}Bytes")
            return archive_name
        else:
            return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
