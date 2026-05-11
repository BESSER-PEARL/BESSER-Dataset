





import java.util.List;
import java.util.ArrayList;

public class testport_Base extends Component {






    private List<testport_Base> testport_bases;


    public testport_Base(
    ) {
        super(
        );
        this.testport_bases = new ArrayList<>();
    }

    public testport_Base(
        ArrayList<testport_Base> testport_bases    ) {
        this.testport_bases = testport_bases;
    }


    public List<testport_Base> getTestport_bases() {
        return testport_bases;
    }

    public void addTestport_base(Testport_base testport_base) {
        this.testport_bases.add(testport_base);
    }

}