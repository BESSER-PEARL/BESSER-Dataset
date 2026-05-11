





import java.util.List;
import java.util.ArrayList;

public class dsl_ExecJava extends Action {

    private String classFqn;
    private String value;
    private String dbSrc;



    public dsl_ExecJava(
        String classFqn,        String value,        String dbSrc    ) {
        super(
        );
        this.classFqn = classFqn;
        this.value = value;
        this.dbSrc = dbSrc;
    }


    public String getClassfqn() {
        return classFqn;
    }

    public void setClassfqn(String classFqn) {
        this.classFqn = classFqn;
    }
    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }
    public String getDbsrc() {
        return dbSrc;
    }

    public void setDbsrc(String dbSrc) {
        this.dbSrc = dbSrc;
    }


}