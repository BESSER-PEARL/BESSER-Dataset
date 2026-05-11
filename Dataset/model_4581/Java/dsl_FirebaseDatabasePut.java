





import java.util.List;
import java.util.ArrayList;

public class dsl_FirebaseDatabasePut extends Action {

    private String value;
    private String fbjson;
    private String url;
    private String dbSrc;
    private String groupPath;
    private String classFqn;



    public dsl_FirebaseDatabasePut(
        String value,        String fbjson,        String url,        String dbSrc,        String groupPath,        String classFqn    ) {
        super(
        );
        this.value = value;
        this.fbjson = fbjson;
        this.url = url;
        this.dbSrc = dbSrc;
        this.groupPath = groupPath;
        this.classFqn = classFqn;
    }


    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }
    public String getFbjson() {
        return fbjson;
    }

    public void setFbjson(String fbjson) {
        this.fbjson = fbjson;
    }
    public String getUrl() {
        return url;
    }

    public void setUrl(String url) {
        this.url = url;
    }
    public String getDbsrc() {
        return dbSrc;
    }

    public void setDbsrc(String dbSrc) {
        this.dbSrc = dbSrc;
    }
    public String getGrouppath() {
        return groupPath;
    }

    public void setGrouppath(String groupPath) {
        this.groupPath = groupPath;
    }
    public String getClassfqn() {
        return classFqn;
    }

    public void setClassfqn(String classFqn) {
        this.classFqn = classFqn;
    }


}