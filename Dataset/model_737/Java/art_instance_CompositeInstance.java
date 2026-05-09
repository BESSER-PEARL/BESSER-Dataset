





import java.util.List;
import java.util.ArrayList;

public class art_instance_CompositeInstance extends ComponentInstance {






    private List<DelegationBinding> delegationbindings;


    public art_instance_CompositeInstance(
    ) {
        super(
        );
        this.delegationbindings = new ArrayList<>();
    }

    public art_instance_CompositeInstance(
        ArrayList<DelegationBinding> delegationbindings    ) {
        this.delegationbindings = delegationbindings;
    }


    public List<DelegationBinding> getDelegationbindings() {
        return delegationbindings;
    }

    public void addDelegationbinding(Delegationbinding delegationbinding) {
        this.delegationbindings.add(delegationbinding);
    }

}