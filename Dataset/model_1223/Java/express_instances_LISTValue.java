





import java.util.List;
import java.util.ArrayList;

public class express_instances_LISTValue extends instances_AggregateValue, core_Instance {






    private List<ListMember> listmembers;


    public express_instances_LISTValue(
    ) {
        super(
        );
        this.listmembers = new ArrayList<>();
    }

    public express_instances_LISTValue(
        ArrayList<ListMember> listmembers    ) {
        this.listmembers = listmembers;
    }


    public List<ListMember> getListmembers() {
        return listmembers;
    }

    public void addListmember(Listmember listmember) {
        this.listmembers.add(listmember);
    }

}