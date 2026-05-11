





import java.util.List;
import java.util.ArrayList;

public class delphi_unitId extends CSTrace {

    private String id;





    private delphi_typeId delphi_typeid;




    private delphi_qualId delphi_qualid;


    public delphi_unitId(
        String id    ) {
        super(
        );
        this.id = id;
    }


    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public delphi_typeId getDelphi_typeid() {
        return delphi_typeid;
    }

    public void setDelphi_typeid(delphi_typeId delphi_typeid) {
        this.delphi_typeid = delphi_typeid;
    }
    public delphi_qualId getDelphi_qualid() {
        return delphi_qualid;
    }

    public void setDelphi_qualid(delphi_qualId delphi_qualid) {
        this.delphi_qualid = delphi_qualid;
    }

}