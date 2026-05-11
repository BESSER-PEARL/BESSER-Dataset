





import java.util.List;
import java.util.ArrayList;

public class party_CommonObject  {






    private List<party_Role> party_roles;




    private party_Role party_role;


    public party_CommonObject(
    ) {
        this.party_roles = new ArrayList<>();
    }

    public party_CommonObject(
        ArrayList<party_Role> party_roles    ) {
        this.party_roles = party_roles;
    }


    public List<party_Role> getParty_roles() {
        return party_roles;
    }

    public void addParty_role(Party_role party_role) {
        this.party_roles.add(party_role);
    }
    public party_Role getParty_role() {
        return party_role;
    }

    public void setParty_role(party_Role party_role) {
        this.party_role = party_role;
    }

}