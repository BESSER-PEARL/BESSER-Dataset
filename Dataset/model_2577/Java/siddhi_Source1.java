





import java.util.List;
import java.util.ArrayList;

public class siddhi_Source1 extends Source1OrStandardStatefulSource {

    private String inner;





    private siddhi_DefinitionAggregation siddhi_definitionaggregation;




    private siddhi_DefinitionStream siddhi_definitionstream;




    private siddhi_DefinitionWindow siddhi_definitionwindow;




    private siddhi_DefinitionTable siddhi_definitiontable;


    public siddhi_Source1(
        String inner    ) {
        super(
        );
        this.inner = inner;
    }


    public String getInner() {
        return inner;
    }

    public void setInner(String inner) {
        this.inner = inner;
    }

    public siddhi_DefinitionAggregation getSiddhi_definitionaggregation() {
        return siddhi_definitionaggregation;
    }

    public void setSiddhi_definitionaggregation(siddhi_DefinitionAggregation siddhi_definitionaggregation) {
        this.siddhi_definitionaggregation = siddhi_definitionaggregation;
    }
    public siddhi_DefinitionStream getSiddhi_definitionstream() {
        return siddhi_definitionstream;
    }

    public void setSiddhi_definitionstream(siddhi_DefinitionStream siddhi_definitionstream) {
        this.siddhi_definitionstream = siddhi_definitionstream;
    }
    public siddhi_DefinitionWindow getSiddhi_definitionwindow() {
        return siddhi_definitionwindow;
    }

    public void setSiddhi_definitionwindow(siddhi_DefinitionWindow siddhi_definitionwindow) {
        this.siddhi_definitionwindow = siddhi_definitionwindow;
    }
    public siddhi_DefinitionTable getSiddhi_definitiontable() {
        return siddhi_definitiontable;
    }

    public void setSiddhi_definitiontable(siddhi_DefinitionTable siddhi_definitiontable) {
        this.siddhi_definitiontable = siddhi_definitiontable;
    }

}