





import java.util.List;
import java.util.ArrayList;

public class simpleocl_CollectionExp extends OclExpression {






    private simpleocl_CollectionPart simpleocl_collectionpart;




    private List<simpleocl_CollectionPart> simpleocl_collectionparts;


    public simpleocl_CollectionExp(
    ) {
        super(
        );
        this.simpleocl_collectionparts = new ArrayList<>();
    }

    public simpleocl_CollectionExp(
        ArrayList<simpleocl_CollectionPart> simpleocl_collectionparts    ) {
        this.simpleocl_collectionparts = simpleocl_collectionparts;
    }


    public simpleocl_CollectionPart getSimpleocl_collectionpart() {
        return simpleocl_collectionpart;
    }

    public void setSimpleocl_collectionpart(simpleocl_CollectionPart simpleocl_collectionpart) {
        this.simpleocl_collectionpart = simpleocl_collectionpart;
    }
    public List<simpleocl_CollectionPart> getSimpleocl_collectionparts() {
        return simpleocl_collectionparts;
    }

    public void addSimpleocl_collectionpart(Simpleocl_collectionpart simpleocl_collectionpart) {
        this.simpleocl_collectionparts.add(simpleocl_collectionpart);
    }

}