





import java.util.List;
import java.util.ArrayList;

public class smallJava_SJMethod extends SJMember {






    private smallJava_SJBlock smalljava_sjblock;




    private List<smallJava_SJParameter> smalljava_sjparameters;


    public smallJava_SJMethod(
    ) {
        super(
        );
        this.smalljava_sjparameters = new ArrayList<>();
    }

    public smallJava_SJMethod(
        ArrayList<smallJava_SJParameter> smalljava_sjparameters    ) {
        this.smalljava_sjparameters = smalljava_sjparameters;
    }


    public smallJava_SJBlock getSmalljava_sjblock() {
        return smalljava_sjblock;
    }

    public void setSmalljava_sjblock(smallJava_SJBlock smalljava_sjblock) {
        this.smalljava_sjblock = smalljava_sjblock;
    }
    public List<smallJava_SJParameter> getSmalljava_sjparameters() {
        return smalljava_sjparameters;
    }

    public void addSmalljava_sjparameter(Smalljava_sjparameter smalljava_sjparameter) {
        this.smalljava_sjparameters.add(smalljava_sjparameter);
    }

}