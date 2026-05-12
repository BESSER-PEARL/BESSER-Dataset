





import java.util.List;
import java.util.ArrayList;

public class sqlDSL_SSettings  {

    private String javapackage;
    private String engine;
    private String schema;





    private sqlDSL_SModel sqldsl_smodel;


    public sqlDSL_SSettings(
        String javapackage,        String engine,        String schema    ) {
        this.javapackage = javapackage;
        this.engine = engine;
        this.schema = schema;
    }


    public String getJavapackage() {
        return javapackage;
    }

    public void setJavapackage(String javapackage) {
        this.javapackage = javapackage;
    }
    public String getEngine() {
        return engine;
    }

    public void setEngine(String engine) {
        this.engine = engine;
    }
    public String getSchema() {
        return schema;
    }

    public void setSchema(String schema) {
        this.schema = schema;
    }

    public sqlDSL_SModel getSqldsl_smodel() {
        return sqldsl_smodel;
    }

    public void setSqldsl_smodel(sqlDSL_SModel sqldsl_smodel) {
        this.sqldsl_smodel = sqldsl_smodel;
    }

}