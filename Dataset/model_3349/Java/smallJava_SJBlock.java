





import java.util.List;
import java.util.ArrayList;

public class smallJava_SJBlock  {






    private List<smallJava_SJStatement> smalljava_sjstatements;


    public smallJava_SJBlock(
    ) {
        this.smalljava_sjstatements = new ArrayList<>();
    }

    public smallJava_SJBlock(
        ArrayList<smallJava_SJStatement> smalljava_sjstatements    ) {
        this.smalljava_sjstatements = smalljava_sjstatements;
    }


    public List<smallJava_SJStatement> getSmalljava_sjstatements() {
        return smalljava_sjstatements;
    }

    public void addSmalljava_sjstatement(Smalljava_sjstatement smalljava_sjstatement) {
        this.smalljava_sjstatements.add(smalljava_sjstatement);
    }

}