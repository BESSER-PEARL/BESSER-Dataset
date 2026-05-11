





import java.util.List;
import java.util.ArrayList;

public class viewpoint_description_DecorationDescriptionsSet  {






    private List<DecorationDescription> decorationdescriptions;


    public viewpoint_description_DecorationDescriptionsSet(
    ) {
        this.decorationdescriptions = new ArrayList<>();
    }

    public viewpoint_description_DecorationDescriptionsSet(
        ArrayList<DecorationDescription> decorationdescriptions    ) {
        this.decorationdescriptions = decorationdescriptions;
    }


    public List<DecorationDescription> getDecorationdescriptions() {
        return decorationdescriptions;
    }

    public void addDecorationdescription(Decorationdescription decorationdescription) {
        this.decorationdescriptions.add(decorationdescription);
    }

}