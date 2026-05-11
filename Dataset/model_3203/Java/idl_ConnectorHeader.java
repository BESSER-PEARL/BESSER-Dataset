





import java.util.List;
import java.util.ArrayList;

public class idl_ConnectorHeader  {

    private String name;





    private idl_ScopedName idl_scopedname;




    private idl_Connector idl_connector;


    public idl_ConnectorHeader(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public idl_ScopedName getIdl_scopedname() {
        return idl_scopedname;
    }

    public void setIdl_scopedname(idl_ScopedName idl_scopedname) {
        this.idl_scopedname = idl_scopedname;
    }
    public idl_Connector getIdl_connector() {
        return idl_connector;
    }

    public void setIdl_connector(idl_Connector idl_connector) {
        this.idl_connector = idl_connector;
    }

}