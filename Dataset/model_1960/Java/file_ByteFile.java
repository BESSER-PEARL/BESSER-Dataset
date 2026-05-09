





import java.util.List;
import java.util.ArrayList;

public class file_ByteFile extends File {

    private String Encoding;



    public file_ByteFile(
        String Encoding    ) {
        super(
        );
        this.Encoding = Encoding;
    }


    public String getEncoding() {
        return Encoding;
    }

    public void setEncoding(String Encoding) {
        this.Encoding = Encoding;
    }


}