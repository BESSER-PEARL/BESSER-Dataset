





import java.util.List;
import java.util.ArrayList;

public class dsl_FirebaseReactiveNotification extends Action {

    private String fbjson;
    private String groupPath;
    private String url;
    private String dbSrc;
    private String classFqn;



    public dsl_FirebaseReactiveNotification(
        String fbjson,        String groupPath,        String url,        String dbSrc,        String classFqn    ) {
        super(
        );
        this.fbjson = fbjson;
        this.groupPath = groupPath;
        this.url = url;
        this.dbSrc = dbSrc;
        this.classFqn = classFqn;
    }


    public String getFbjson() {
        return fbjson;
    }

    public void setFbjson(String fbjson) {
        this.fbjson = fbjson;
    }
    public String getGrouppath() {
        return groupPath;
    }

    public void setGrouppath(String groupPath) {
        this.groupPath = groupPath;
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
    public String getClassfqn() {
        return classFqn;
    }

    public void setClassfqn(String classFqn) {
        this.classFqn = classFqn;
    }


}