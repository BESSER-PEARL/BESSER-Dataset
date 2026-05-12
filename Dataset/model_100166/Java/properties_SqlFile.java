





import java.util.List;
import java.util.ArrayList;

public class properties_SqlFile extends Sql {

    private String filePath;





    private properties_SpecificDBMSProperties properties_specificdbmsproperties;


    public properties_SqlFile(
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

    public properties_SpecificDBMSProperties getProperties_specificdbmsproperties() {
        return properties_specificdbmsproperties;
    }

    public void setProperties_specificdbmsproperties(properties_SpecificDBMSProperties properties_specificdbmsproperties) {
        this.properties_specificdbmsproperties = properties_specificdbmsproperties;
    }

}