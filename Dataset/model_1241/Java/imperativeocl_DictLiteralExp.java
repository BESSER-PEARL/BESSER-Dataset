





import java.util.List;
import java.util.ArrayList;

public class imperativeocl_DictLiteralExp  {






    private List<DictLiteralPart> dictliteralparts;


    public imperativeocl_DictLiteralExp(
    ) {
        this.dictliteralparts = new ArrayList<>();
    }

    public imperativeocl_DictLiteralExp(
        ArrayList<DictLiteralPart> dictliteralparts    ) {
        this.dictliteralparts = dictliteralparts;
    }


    public List<DictLiteralPart> getDictliteralparts() {
        return dictliteralparts;
    }

    public void addDictliteralpart(Dictliteralpart dictliteralpart) {
        this.dictliteralparts.add(dictliteralpart);
    }

}