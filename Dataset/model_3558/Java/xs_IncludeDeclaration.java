





import java.util.List;
import java.util.ArrayList;

public class xs_IncludeDeclaration extends Declaration {

    private String filePath;



    public xs_IncludeDeclaration(
        String filePath    ) {
        super(
        );
        this.filePath = filePath;
    }


    public String getFilepath() {
        return filePath;
    }

    public void setFilepath(String filePath) {
        this.filePath = filePath;
    }


}