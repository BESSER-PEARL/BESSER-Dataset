





import java.util.List;
import java.util.ArrayList;

public class sqlmodel_schema_Dependency extends SQLObject {

    private String dependencyType;



    public sqlmodel_schema_Dependency(
        String dependencyType    ) {
        super(
        );
        this.dependencyType = dependencyType;
    }


    public String getDependencytype() {
        return dependencyType;
    }

    public void setDependencytype(String dependencyType) {
        this.dependencyType = dependencyType;
    }


}