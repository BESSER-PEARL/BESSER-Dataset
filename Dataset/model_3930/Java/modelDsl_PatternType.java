





import java.util.List;
import java.util.ArrayList;

public class modelDsl_PatternType  {

    private String NUMBER;
    private String REGEX;
    private String DATE;





    private modelDsl_DataTypeField modeldsl_datatypefield;


    public modelDsl_PatternType(
        String NUMBER,        String REGEX,        String DATE    ) {
        this.NUMBER = NUMBER;
        this.REGEX = REGEX;
        this.DATE = DATE;
    }


    public String getNumber() {
        return NUMBER;
    }

    public void setNumber(String NUMBER) {
        this.NUMBER = NUMBER;
    }
    public String getRegex() {
        return REGEX;
    }

    public void setRegex(String REGEX) {
        this.REGEX = REGEX;
    }
    public String getDate() {
        return DATE;
    }

    public void setDate(String DATE) {
        this.DATE = DATE;
    }

    public modelDsl_DataTypeField getModeldsl_datatypefield() {
        return modeldsl_datatypefield;
    }

    public void setModeldsl_datatypefield(modelDsl_DataTypeField modeldsl_datatypefield) {
        this.modeldsl_datatypefield = modeldsl_datatypefield;
    }

}