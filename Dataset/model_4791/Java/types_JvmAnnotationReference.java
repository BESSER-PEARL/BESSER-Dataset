





import java.util.List;
import java.util.ArrayList;

public class types_JvmAnnotationReference  {






    private List<types_JvmAnnotationValue> types_jvmannotationvalues;




    private types_JvmAnnotationTarget types_jvmannotationtarget;




    private types_JvmAnnotationTarget types_jvmannotationtarget;




    private types_JvmAnnotationType types_jvmannotationtype;




    private types_JvmAnnotationAnnotationValue types_jvmannotationannotationvalue;


    public types_JvmAnnotationReference(
    ) {
        this.types_jvmannotationvalues = new ArrayList<>();
    }

    public types_JvmAnnotationReference(
        ArrayList<types_JvmAnnotationValue> types_jvmannotationvalues    ) {
        this.types_jvmannotationvalues = types_jvmannotationvalues;
    }


    public List<types_JvmAnnotationValue> getTypes_jvmannotationvalues() {
        return types_jvmannotationvalues;
    }

    public void addTypes_jvmannotationvalue(Types_jvmannotationvalue types_jvmannotationvalue) {
        this.types_jvmannotationvalues.add(types_jvmannotationvalue);
    }
    public types_JvmAnnotationTarget getTypes_jvmannotationtarget() {
        return types_jvmannotationtarget;
    }

    public void setTypes_jvmannotationtarget(types_JvmAnnotationTarget types_jvmannotationtarget) {
        this.types_jvmannotationtarget = types_jvmannotationtarget;
    }
    public types_JvmAnnotationTarget getTypes_jvmannotationtarget() {
        return types_jvmannotationtarget;
    }

    public void setTypes_jvmannotationtarget(types_JvmAnnotationTarget types_jvmannotationtarget) {
        this.types_jvmannotationtarget = types_jvmannotationtarget;
    }
    public types_JvmAnnotationType getTypes_jvmannotationtype() {
        return types_jvmannotationtype;
    }

    public void setTypes_jvmannotationtype(types_JvmAnnotationType types_jvmannotationtype) {
        this.types_jvmannotationtype = types_jvmannotationtype;
    }
    public types_JvmAnnotationAnnotationValue getTypes_jvmannotationannotationvalue() {
        return types_jvmannotationannotationvalue;
    }

    public void setTypes_jvmannotationannotationvalue(types_JvmAnnotationAnnotationValue types_jvmannotationannotationvalue) {
        this.types_jvmannotationannotationvalue = types_jvmannotationannotationvalue;
    }

}