





import java.util.List;
import java.util.ArrayList;

public class model_User extends Node {

    private String isBlocked;
    private String isEditor;
    private String isReader;
    private String typePrefix;



    public model_User(
        String isBlocked,        String isEditor,        String isReader,        String typePrefix    ) {
        super(
        );
        this.isBlocked = isBlocked;
        this.isEditor = isEditor;
        this.isReader = isReader;
        this.typePrefix = typePrefix;
    }


    public String getIsblocked() {
        return isBlocked;
    }

    public void setIsblocked(String isBlocked) {
        this.isBlocked = isBlocked;
    }
    public String getIseditor() {
        return isEditor;
    }

    public void setIseditor(String isEditor) {
        this.isEditor = isEditor;
    }
    public String getIsreader() {
        return isReader;
    }

    public void setIsreader(String isReader) {
        this.isReader = isReader;
    }
    public String getTypeprefix() {
        return typePrefix;
    }

    public void setTypeprefix(String typePrefix) {
        this.typePrefix = typePrefix;
    }


}