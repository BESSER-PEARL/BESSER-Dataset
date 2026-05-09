





import java.util.List;
import java.util.ArrayList;

public class file_FileOwner  {






    private List<file_File> file_files;


    public file_FileOwner(
    ) {
        this.file_files = new ArrayList<>();
    }

    public file_FileOwner(
        ArrayList<file_File> file_files    ) {
        this.file_files = file_files;
    }


    public List<file_File> getFile_files() {
        return file_files;
    }

    public void addFile_file(File_file file_file) {
        this.file_files.add(file_file);
    }

}