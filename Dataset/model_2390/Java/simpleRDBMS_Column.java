





import java.util.List;
import java.util.ArrayList;

public class simpleRDBMS_Column extends NamedElement {






    private simpleRDBMS_Key simplerdbms_key;




    private simpleRDBMS_ForeignKey simplerdbms_foreignkey;




    private simpleRDBMS_Table simplerdbms_table;


    public simpleRDBMS_Column(
    ) {
        super(
        );
    }



    public simpleRDBMS_Key getSimplerdbms_key() {
        return simplerdbms_key;
    }

    public void setSimplerdbms_key(simpleRDBMS_Key simplerdbms_key) {
        this.simplerdbms_key = simplerdbms_key;
    }
    public simpleRDBMS_ForeignKey getSimplerdbms_foreignkey() {
        return simplerdbms_foreignkey;
    }

    public void setSimplerdbms_foreignkey(simpleRDBMS_ForeignKey simplerdbms_foreignkey) {
        this.simplerdbms_foreignkey = simplerdbms_foreignkey;
    }
    public simpleRDBMS_Table getSimplerdbms_table() {
        return simplerdbms_table;
    }

    public void setSimplerdbms_table(simpleRDBMS_Table simplerdbms_table) {
        this.simplerdbms_table = simplerdbms_table;
    }

}