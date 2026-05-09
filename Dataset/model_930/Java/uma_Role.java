





import java.util.List;
import java.util.ArrayList;

public class uma_Role extends ContentElement {






    private uma_RoleSet uma_roleset;




    private uma_RoleDescriptor uma_roledescriptor;




    private uma_CompositeRole uma_compositerole;


    public uma_Role(
    ) {
        super(
        );
    }



    public uma_RoleSet getUma_roleset() {
        return uma_roleset;
    }

    public void setUma_roleset(uma_RoleSet uma_roleset) {
        this.uma_roleset = uma_roleset;
    }
    public uma_RoleDescriptor getUma_roledescriptor() {
        return uma_roledescriptor;
    }

    public void setUma_roledescriptor(uma_RoleDescriptor uma_roledescriptor) {
        this.uma_roledescriptor = uma_roledescriptor;
    }
    public uma_CompositeRole getUma_compositerole() {
        return uma_compositerole;
    }

    public void setUma_compositerole(uma_CompositeRole uma_compositerole) {
        this.uma_compositerole = uma_compositerole;
    }

}