





import java.util.List;
import java.util.ArrayList;

public class xtend_JvmAnnotationReference  {






    private xtend_JvmAnnotationType xtend_jvmannotationtype;




    private xtend_JvmAnnotationAnnotationValue xtend_jvmannotationannotationvalue;




    private xtend_JvmAnnotationTarget xtend_jvmannotationtarget;




    private List<xtend_JvmAnnotationValue> xtend_jvmannotationvalues;




    private xtend_JvmAnnotationTarget xtend_jvmannotationtarget;


    public xtend_JvmAnnotationReference(
    ) {
        this.xtend_jvmannotationvalues = new ArrayList<>();
    }

    public xtend_JvmAnnotationReference(
        ArrayList<xtend_JvmAnnotationValue> xtend_jvmannotationvalues    ) {
        this.xtend_jvmannotationvalues = xtend_jvmannotationvalues;
    }


    public xtend_JvmAnnotationType getXtend_jvmannotationtype() {
        return xtend_jvmannotationtype;
    }

    public void setXtend_jvmannotationtype(xtend_JvmAnnotationType xtend_jvmannotationtype) {
        this.xtend_jvmannotationtype = xtend_jvmannotationtype;
    }
    public xtend_JvmAnnotationAnnotationValue getXtend_jvmannotationannotationvalue() {
        return xtend_jvmannotationannotationvalue;
    }

    public void setXtend_jvmannotationannotationvalue(xtend_JvmAnnotationAnnotationValue xtend_jvmannotationannotationvalue) {
        this.xtend_jvmannotationannotationvalue = xtend_jvmannotationannotationvalue;
    }
    public xtend_JvmAnnotationTarget getXtend_jvmannotationtarget() {
        return xtend_jvmannotationtarget;
    }

    public void setXtend_jvmannotationtarget(xtend_JvmAnnotationTarget xtend_jvmannotationtarget) {
        this.xtend_jvmannotationtarget = xtend_jvmannotationtarget;
    }
    public List<xtend_JvmAnnotationValue> getXtend_jvmannotationvalues() {
        return xtend_jvmannotationvalues;
    }

    public void addXtend_jvmannotationvalue(Xtend_jvmannotationvalue xtend_jvmannotationvalue) {
        this.xtend_jvmannotationvalues.add(xtend_jvmannotationvalue);
    }
    public xtend_JvmAnnotationTarget getXtend_jvmannotationtarget() {
        return xtend_jvmannotationtarget;
    }

    public void setXtend_jvmannotationtarget(xtend_JvmAnnotationTarget xtend_jvmannotationtarget) {
        this.xtend_jvmannotationtarget = xtend_jvmannotationtarget;
    }

}