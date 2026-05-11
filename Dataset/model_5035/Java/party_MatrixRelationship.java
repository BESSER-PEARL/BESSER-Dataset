





import java.util.List;
import java.util.ArrayList;

public class party_MatrixRelationship extends DateEffectiveObject {

    private String name;





    private party_Organization party_organization;


    public party_MatrixRelationship(
        String name    ) {
        super(
        );
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public party_Organization getParty_organization() {
        return party_organization;
    }

    public void setParty_organization(party_Organization party_organization) {
        this.party_organization = party_organization;
    }

}