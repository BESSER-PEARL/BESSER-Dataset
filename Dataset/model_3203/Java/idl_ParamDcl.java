





import java.util.List;
import java.util.ArrayList;

public class idl_ParamDcl  {

    private String name;
    private String direction;





    private idl_ParameterDecls idl_parameterdecls;




    private idl_ParamTypeSpec idl_paramtypespec;


    public idl_ParamDcl(
        String name,        String direction    ) {
        this.name = name;
        this.direction = direction;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getDirection() {
        return direction;
    }

    public void setDirection(String direction) {
        this.direction = direction;
    }

    public idl_ParameterDecls getIdl_parameterdecls() {
        return idl_parameterdecls;
    }

    public void setIdl_parameterdecls(idl_ParameterDecls idl_parameterdecls) {
        this.idl_parameterdecls = idl_parameterdecls;
    }
    public idl_ParamTypeSpec getIdl_paramtypespec() {
        return idl_paramtypespec;
    }

    public void setIdl_paramtypespec(idl_ParamTypeSpec idl_paramtypespec) {
        this.idl_paramtypespec = idl_paramtypespec;
    }

}