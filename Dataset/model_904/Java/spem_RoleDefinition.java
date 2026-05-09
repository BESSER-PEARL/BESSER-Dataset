





import java.util.List;
import java.util.ArrayList;

public class spem_RoleDefinition extends MethodContentElement {

    private String synonym;





    private spem_RoleUse spem_roleuse;


    public spem_RoleDefinition(
        String synonym    ) {
        super(
        );
        this.synonym = synonym;
    }


    public String getSynonym() {
        return synonym;
    }

    public void setSynonym(String synonym) {
        this.synonym = synonym;
    }

    public spem_RoleUse getSpem_roleuse() {
        return spem_roleuse;
    }

    public void setSpem_roleuse(spem_RoleUse spem_roleuse) {
        this.spem_roleuse = spem_roleuse;
    }

}