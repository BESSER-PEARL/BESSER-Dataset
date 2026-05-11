





import java.util.List;
import java.util.ArrayList;

public class DiagonosticModel_TestSpecification  {

    private String version;
    private String functionVersion;
    private String name;
    private String description;
    private String functionName;
    private String author;



    public DiagonosticModel_TestSpecification(
        String version,        String functionVersion,        String name,        String description,        String functionName,        String author    ) {
        this.version = version;
        this.functionVersion = functionVersion;
        this.name = name;
        this.description = description;
        this.functionName = functionName;
        this.author = author;
    }


    public String getVersion() {
        return version;
    }

    public void setVersion(String version) {
        this.version = version;
    }
    public String getFunctionversion() {
        return functionVersion;
    }

    public void setFunctionversion(String functionVersion) {
        this.functionVersion = functionVersion;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public String getFunctionname() {
        return functionName;
    }

    public void setFunctionname(String functionName) {
        this.functionName = functionName;
    }
    public String getAuthor() {
        return author;
    }

    public void setAuthor(String author) {
        this.author = author;
    }


}