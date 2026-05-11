





import java.util.List;
import java.util.ArrayList;

public class vcml_NumberList extends List {






    private List<vcml_NumberListEntry> vcml_numberlistentrys;


    public vcml_NumberList(
    ) {
        super(
        );
        this.vcml_numberlistentrys = new ArrayList<>();
    }

    public vcml_NumberList(
        ArrayList<vcml_NumberListEntry> vcml_numberlistentrys    ) {
        this.vcml_numberlistentrys = vcml_numberlistentrys;
    }


    public List<vcml_NumberListEntry> getVcml_numberlistentrys() {
        return vcml_numberlistentrys;
    }

    public void addVcml_numberlistentry(Vcml_numberlistentry vcml_numberlistentry) {
        this.vcml_numberlistentrys.add(vcml_numberlistentry);
    }

}