





import java.util.List;
import java.util.ArrayList;

public class delphi_fieldDecl extends CSTrace {

    private String port;





    private delphi_identList delphi_identlist;




    private delphi_fieldList delphi_fieldlist;




    private delphi_type delphi_type;


    public delphi_fieldDecl(
        String port    ) {
        super(
        );
        this.port = port;
    }


    public String getPort() {
        return port;
    }

    public void setPort(String port) {
        this.port = port;
    }

    public delphi_identList getDelphi_identlist() {
        return delphi_identlist;
    }

    public void setDelphi_identlist(delphi_identList delphi_identlist) {
        this.delphi_identlist = delphi_identlist;
    }
    public delphi_fieldList getDelphi_fieldlist() {
        return delphi_fieldlist;
    }

    public void setDelphi_fieldlist(delphi_fieldList delphi_fieldlist) {
        this.delphi_fieldlist = delphi_fieldlist;
    }
    public delphi_type getDelphi_type() {
        return delphi_type;
    }

    public void setDelphi_type(delphi_type delphi_type) {
        this.delphi_type = delphi_type;
    }

}