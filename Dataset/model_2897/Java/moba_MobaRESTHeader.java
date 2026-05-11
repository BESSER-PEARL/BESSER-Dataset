





import java.util.List;
import java.util.ArrayList;

public class moba_MobaRESTHeader  {

    private String keyString;
    private boolean contentTypeHeader;
    private boolean rawHeader;
    private String key;
    private String valueString;
    private String value;





    private moba_MobaConstant moba_mobaconstant;




    private moba_MobaConstant moba_mobaconstant;




    private moba_MobaREST moba_mobarest;


    public moba_MobaRESTHeader(
        String keyString,        boolean contentTypeHeader,        boolean rawHeader,        String key,        String valueString,        String value    ) {
        this.keyString = keyString;
        this.contentTypeHeader = contentTypeHeader;
        this.rawHeader = rawHeader;
        this.key = key;
        this.valueString = valueString;
        this.value = value;
    }


    public String getKeystring() {
        return keyString;
    }

    public void setKeystring(String keyString) {
        this.keyString = keyString;
    }
    public boolean getContenttypeheader() {
        return contentTypeHeader;
    }

    public void setContenttypeheader(boolean contentTypeHeader) {
        this.contentTypeHeader = contentTypeHeader;
    }
    public boolean getRawheader() {
        return rawHeader;
    }

    public void setRawheader(boolean rawHeader) {
        this.rawHeader = rawHeader;
    }
    public String getKey() {
        return key;
    }

    public void setKey(String key) {
        this.key = key;
    }
    public String getValuestring() {
        return valueString;
    }

    public void setValuestring(String valueString) {
        this.valueString = valueString;
    }
    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }

    public moba_MobaConstant getMoba_mobaconstant() {
        return moba_mobaconstant;
    }

    public void setMoba_mobaconstant(moba_MobaConstant moba_mobaconstant) {
        this.moba_mobaconstant = moba_mobaconstant;
    }
    public moba_MobaConstant getMoba_mobaconstant() {
        return moba_mobaconstant;
    }

    public void setMoba_mobaconstant(moba_MobaConstant moba_mobaconstant) {
        this.moba_mobaconstant = moba_mobaconstant;
    }
    public moba_MobaREST getMoba_mobarest() {
        return moba_mobarest;
    }

    public void setMoba_mobarest(moba_MobaREST moba_mobarest) {
        this.moba_mobarest = moba_mobarest;
    }

}