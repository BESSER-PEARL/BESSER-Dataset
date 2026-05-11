





import java.util.List;
import java.util.ArrayList;

public class moba_MobaRESTAbstractAttribute  {

    private String aliasString;
    private String alias;
    private boolean attachment;





    private moba_MobaConstant moba_mobaconstant;




    private moba_MobaRESTCustomService moba_mobarestcustomservice;




    private moba_MobaRESTCustomService moba_mobarestcustomservice;


    public moba_MobaRESTAbstractAttribute(
        String aliasString,        String alias,        boolean attachment    ) {
        this.aliasString = aliasString;
        this.alias = alias;
        this.attachment = attachment;
    }


    public String getAliasstring() {
        return aliasString;
    }

    public void setAliasstring(String aliasString) {
        this.aliasString = aliasString;
    }
    public String getAlias() {
        return alias;
    }

    public void setAlias(String alias) {
        this.alias = alias;
    }
    public boolean getAttachment() {
        return attachment;
    }

    public void setAttachment(boolean attachment) {
        this.attachment = attachment;
    }

    public moba_MobaConstant getMoba_mobaconstant() {
        return moba_mobaconstant;
    }

    public void setMoba_mobaconstant(moba_MobaConstant moba_mobaconstant) {
        this.moba_mobaconstant = moba_mobaconstant;
    }
    public moba_MobaRESTCustomService getMoba_mobarestcustomservice() {
        return moba_mobarestcustomservice;
    }

    public void setMoba_mobarestcustomservice(moba_MobaRESTCustomService moba_mobarestcustomservice) {
        this.moba_mobarestcustomservice = moba_mobarestcustomservice;
    }
    public moba_MobaRESTCustomService getMoba_mobarestcustomservice() {
        return moba_mobarestcustomservice;
    }

    public void setMoba_mobarestcustomservice(moba_MobaRESTCustomService moba_mobarestcustomservice) {
        this.moba_mobarestcustomservice = moba_mobarestcustomservice;
    }

}