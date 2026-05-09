





import java.util.List;
import java.util.ArrayList;

public class uml_Operation extends BehavioralFeature {

    private String upper;
    private String isUnique;
    private String isQuery;
    private String isOrdered;
    private String lower;





    private uml_Parameter uml_parameter;




    private uml_Operation uml_operation;




    private uml_Class uml_class;




    private uml_Class uml_class;


    public uml_Operation(
        String upper,        String isUnique,        String isQuery,        String isOrdered,        String lower    ) {
        super(
        );
        this.upper = upper;
        this.isUnique = isUnique;
        this.isQuery = isQuery;
        this.isOrdered = isOrdered;
        this.lower = lower;
    }


    public String getUpper() {
        return upper;
    }

    public void setUpper(String upper) {
        this.upper = upper;
    }
    public String getIsunique() {
        return isUnique;
    }

    public void setIsunique(String isUnique) {
        this.isUnique = isUnique;
    }
    public String getIsquery() {
        return isQuery;
    }

    public void setIsquery(String isQuery) {
        this.isQuery = isQuery;
    }
    public String getIsordered() {
        return isOrdered;
    }

    public void setIsordered(String isOrdered) {
        this.isOrdered = isOrdered;
    }
    public String getLower() {
        return lower;
    }

    public void setLower(String lower) {
        this.lower = lower;
    }

    public uml_Parameter getUml_parameter() {
        return uml_parameter;
    }

    public void setUml_parameter(uml_Parameter uml_parameter) {
        this.uml_parameter = uml_parameter;
    }
    public uml_Operation getUml_operation() {
        return uml_operation;
    }

    public void setUml_operation(uml_Operation uml_operation) {
        this.uml_operation = uml_operation;
    }
    public uml_Class getUml_class() {
        return uml_class;
    }

    public void setUml_class(uml_Class uml_class) {
        this.uml_class = uml_class;
    }
    public uml_Class getUml_class() {
        return uml_class;
    }

    public void setUml_class(uml_Class uml_class) {
        this.uml_class = uml_class;
    }

}