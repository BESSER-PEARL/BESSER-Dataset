





import java.util.List;
import java.util.ArrayList;

public class wsn_OpaqueAction extends , Action {

    private String language;
    private String code;
    private String type;
    private String file;



    public wsn_OpaqueAction(
        String language,        String code,        String type,        String file    ) {
        super(
        );
        this.language = language;
        this.code = code;
        this.type = type;
        this.file = file;
    }


    public String getLanguage() {
        return language;
    }

    public void setLanguage(String language) {
        this.language = language;
    }
    public String getCode() {
        return code;
    }

    public void setCode(String code) {
        this.code = code;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getFile() {
        return file;
    }

    public void setFile(String file) {
        this.file = file;
    }


}