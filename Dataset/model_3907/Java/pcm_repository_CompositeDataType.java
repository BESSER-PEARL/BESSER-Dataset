





import java.util.List;
import java.util.ArrayList;

public class pcm_repository_CompositeDataType extends repository_DataType, entity_Entity {






    private List<InnerDeclaration> innerdeclarations;




    private List<CompositeDataType> compositedatatypes;


    public pcm_repository_CompositeDataType(
    ) {
        super(
        );
        this.innerdeclarations = new ArrayList<>();
        this.compositedatatypes = new ArrayList<>();
    }

    public pcm_repository_CompositeDataType(
        ArrayList<InnerDeclaration> innerdeclarations,        ArrayList<CompositeDataType> compositedatatypes    ) {
        this.innerdeclarations = innerdeclarations;
        this.compositedatatypes = compositedatatypes;
    }


    public List<InnerDeclaration> getInnerdeclarations() {
        return innerdeclarations;
    }

    public void addInnerdeclaration(Innerdeclaration innerdeclaration) {
        this.innerdeclarations.add(innerdeclaration);
    }
    public List<CompositeDataType> getCompositedatatypes() {
        return compositedatatypes;
    }

    public void addCompositedatatype(Compositedatatype compositedatatype) {
        this.compositedatatypes.add(compositedatatype);
    }

}