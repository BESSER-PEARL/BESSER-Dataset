





import java.util.List;
import java.util.ArrayList;

public class rif11a_ExchangeFile_AttributeValueFileReference extends AttributeValueComplex {

    private String pathToFile;



    public rif11a_ExchangeFile_AttributeValueFileReference(
        String pathToFile    ) {
        super(
        );
        this.pathToFile = pathToFile;
    }


    public String getPathtofile() {
        return pathToFile;
    }

    public void setPathtofile(String pathToFile) {
        this.pathToFile = pathToFile;
    }


}