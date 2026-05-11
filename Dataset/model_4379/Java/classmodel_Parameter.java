





import java.util.List;
import java.util.ArrayList;

public class classmodel_Parameter  {

    private String implicit;
    private String name;





    private classmodel_Operation classmodel_operation;


    public classmodel_Parameter(
        String implicit,        String name    ) {
        this.implicit = implicit;
        this.name = name;
    }


    public String getImplicit() {
        return implicit;
    }

    public void setImplicit(String implicit) {
        this.implicit = implicit;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public classmodel_Operation getClassmodel_operation() {
        return classmodel_operation;
    }

    public void setClassmodel_operation(classmodel_Operation classmodel_operation) {
        this.classmodel_operation = classmodel_operation;
    }

}