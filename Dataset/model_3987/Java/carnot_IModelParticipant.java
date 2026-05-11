





import java.util.List;
import java.util.ArrayList;

public class carnot_IModelParticipant extends IIdentifiableModelElement {






    private carnot_ISwimlaneSymbol carnot_iswimlanesymbol;




    private carnot_ISwimlaneSymbol carnot_iswimlanesymbol;




    private List<carnot_ISwimlaneSymbol> carnot_iswimlanesymbols;


    public carnot_IModelParticipant(
    ) {
        super(
        );
        this.carnot_iswimlanesymbols = new ArrayList<>();
    }

    public carnot_IModelParticipant(
        ArrayList<carnot_ISwimlaneSymbol> carnot_iswimlanesymbols    ) {
        this.carnot_iswimlanesymbols = carnot_iswimlanesymbols;
    }


    public carnot_ISwimlaneSymbol getCarnot_iswimlanesymbol() {
        return carnot_iswimlanesymbol;
    }

    public void setCarnot_iswimlanesymbol(carnot_ISwimlaneSymbol carnot_iswimlanesymbol) {
        this.carnot_iswimlanesymbol = carnot_iswimlanesymbol;
    }
    public carnot_ISwimlaneSymbol getCarnot_iswimlanesymbol() {
        return carnot_iswimlanesymbol;
    }

    public void setCarnot_iswimlanesymbol(carnot_ISwimlaneSymbol carnot_iswimlanesymbol) {
        this.carnot_iswimlanesymbol = carnot_iswimlanesymbol;
    }
    public List<carnot_ISwimlaneSymbol> getCarnot_iswimlanesymbols() {
        return carnot_iswimlanesymbols;
    }

    public void addCarnot_iswimlanesymbol(Carnot_iswimlanesymbol carnot_iswimlanesymbol) {
        this.carnot_iswimlanesymbols.add(carnot_iswimlanesymbol);
    }

}