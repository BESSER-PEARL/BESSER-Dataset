





import java.util.List;
import java.util.ArrayList;

public class sADL_SadlTypeReference extends SadlStatement {






    private sADL_SadlInstance sadl_sadlinstance;




    private sADL_SadlClassOrPropertyDeclaration sadl_sadlclassorpropertydeclaration;




    private sADL_SadlSameAs sadl_sadlsameas;




    private sADL_SadlDifferentFrom sadl_sadldifferentfrom;


    public sADL_SadlTypeReference(
    ) {
        super(
        );
    }



    public sADL_SadlInstance getSadl_sadlinstance() {
        return sadl_sadlinstance;
    }

    public void setSadl_sadlinstance(sADL_SadlInstance sadl_sadlinstance) {
        this.sadl_sadlinstance = sadl_sadlinstance;
    }
    public sADL_SadlClassOrPropertyDeclaration getSadl_sadlclassorpropertydeclaration() {
        return sadl_sadlclassorpropertydeclaration;
    }

    public void setSadl_sadlclassorpropertydeclaration(sADL_SadlClassOrPropertyDeclaration sadl_sadlclassorpropertydeclaration) {
        this.sadl_sadlclassorpropertydeclaration = sadl_sadlclassorpropertydeclaration;
    }
    public sADL_SadlSameAs getSadl_sadlsameas() {
        return sadl_sadlsameas;
    }

    public void setSadl_sadlsameas(sADL_SadlSameAs sadl_sadlsameas) {
        this.sadl_sadlsameas = sadl_sadlsameas;
    }
    public sADL_SadlDifferentFrom getSadl_sadldifferentfrom() {
        return sadl_sadldifferentfrom;
    }

    public void setSadl_sadldifferentfrom(sADL_SadlDifferentFrom sadl_sadldifferentfrom) {
        this.sadl_sadldifferentfrom = sadl_sadldifferentfrom;
    }

}