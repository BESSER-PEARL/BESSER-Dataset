





import java.util.List;
import java.util.ArrayList;

public class frameweb_VocabularyClass extends VocabularyEntity, VocabularyClassExpression {






    private List<frameweb_VocabularyProperty> frameweb_vocabularypropertys;


    public frameweb_VocabularyClass(
    ) {
        super(
        );
        this.frameweb_vocabularypropertys = new ArrayList<>();
    }

    public frameweb_VocabularyClass(
        ArrayList<frameweb_VocabularyProperty> frameweb_vocabularypropertys    ) {
        this.frameweb_vocabularypropertys = frameweb_vocabularypropertys;
    }


    public List<frameweb_VocabularyProperty> getFrameweb_vocabularypropertys() {
        return frameweb_vocabularypropertys;
    }

    public void addFrameweb_vocabularyproperty(Frameweb_vocabularyproperty frameweb_vocabularyproperty) {
        this.frameweb_vocabularypropertys.add(frameweb_vocabularyproperty);
    }

}