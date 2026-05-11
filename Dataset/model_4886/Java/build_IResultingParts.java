





import java.util.List;
import java.util.ArrayList;

public class build_IResultingParts extends IActionResult {






    private build_IProducedPart build_iproducedpart;




    private List<build_IProducedPart> build_iproducedparts;


    public build_IResultingParts(
    ) {
        super(
        );
        this.build_iproducedparts = new ArrayList<>();
    }

    public build_IResultingParts(
        ArrayList<build_IProducedPart> build_iproducedparts    ) {
        this.build_iproducedparts = build_iproducedparts;
    }


    public build_IProducedPart getBuild_iproducedpart() {
        return build_iproducedpart;
    }

    public void setBuild_iproducedpart(build_IProducedPart build_iproducedpart) {
        this.build_iproducedpart = build_iproducedpart;
    }
    public List<build_IProducedPart> getBuild_iproducedparts() {
        return build_iproducedparts;
    }

    public void addBuild_iproducedpart(Build_iproducedpart build_iproducedpart) {
        this.build_iproducedparts.add(build_iproducedpart);
    }

}