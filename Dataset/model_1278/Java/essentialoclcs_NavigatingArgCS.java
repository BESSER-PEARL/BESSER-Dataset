





import java.util.List;
import java.util.ArrayList;

public class essentialoclcs_NavigatingArgCS extends ModelElementCS {

    private String role;
    private String prefix;





    private essentialoclcs_ExpCS essentialoclcs_expcs;




    private essentialoclcs_ExpCS essentialoclcs_expcs;


    public essentialoclcs_NavigatingArgCS(
        String role,        String prefix    ) {
        super(
        );
        this.role = role;
        this.prefix = prefix;
    }


    public String getRole() {
        return role;
    }

    public void setRole(String role) {
        this.role = role;
    }
    public String getPrefix() {
        return prefix;
    }

    public void setPrefix(String prefix) {
        this.prefix = prefix;
    }

    public essentialoclcs_ExpCS getEssentialoclcs_expcs() {
        return essentialoclcs_expcs;
    }

    public void setEssentialoclcs_expcs(essentialoclcs_ExpCS essentialoclcs_expcs) {
        this.essentialoclcs_expcs = essentialoclcs_expcs;
    }
    public essentialoclcs_ExpCS getEssentialoclcs_expcs() {
        return essentialoclcs_expcs;
    }

    public void setEssentialoclcs_expcs(essentialoclcs_ExpCS essentialoclcs_expcs) {
        this.essentialoclcs_expcs = essentialoclcs_expcs;
    }

}