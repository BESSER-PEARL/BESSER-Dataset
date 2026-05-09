





import java.util.List;
import java.util.ArrayList;

public class file_FileLocal extends ByteFile {

    private String FilePath;



    public file_FileLocal(
        String FilePath    ) {
        super(
        );
        this.FilePath = FilePath;
    }


    public String getFilepath() {
        return FilePath;
    }

    public void setFilepath(String FilePath) {
        this.FilePath = FilePath;
    }


}