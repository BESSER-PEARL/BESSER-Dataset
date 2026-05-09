





import java.util.List;
import java.util.ArrayList;

public class Arch_Method  {

    private String returntype;
    private String name;





    private Arch_Logic arch_logic;




    private Arch_Entity arch_entity;




    private Arch_Service arch_service;


    public Arch_Method(
        String returntype,        String name    ) {
        this.returntype = returntype;
        this.name = name;
    }


    public String getReturntype() {
        return returntype;
    }

    public void setReturntype(String returntype) {
        this.returntype = returntype;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public Arch_Logic getArch_logic() {
        return arch_logic;
    }

    public void setArch_logic(Arch_Logic arch_logic) {
        this.arch_logic = arch_logic;
    }
    public Arch_Entity getArch_entity() {
        return arch_entity;
    }

    public void setArch_entity(Arch_Entity arch_entity) {
        this.arch_entity = arch_entity;
    }
    public Arch_Service getArch_service() {
        return arch_service;
    }

    public void setArch_service(Arch_Service arch_service) {
        this.arch_service = arch_service;
    }

}