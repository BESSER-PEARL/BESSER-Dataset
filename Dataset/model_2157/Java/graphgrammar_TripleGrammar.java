





import java.util.List;
import java.util.ArrayList;

public class graphgrammar_TripleGrammar  {

    private String name;





    private List<graphgrammar_Symbol> graphgrammar_symbols;




    private List<graphgrammar_Symbol> graphgrammar_symbols;




    private List<graphgrammar_Symbol> graphgrammar_symbols;




    private graphgrammar_Symbol graphgrammar_symbol;


    public graphgrammar_TripleGrammar(
        String name    ) {
        this.name = name;
        this.graphgrammar_symbols = new ArrayList<>();
        this.graphgrammar_symbols = new ArrayList<>();
        this.graphgrammar_symbols = new ArrayList<>();
    }

    public graphgrammar_TripleGrammar(
        String name        ArrayList<graphgrammar_Symbol> graphgrammar_symbols,        ArrayList<graphgrammar_Symbol> graphgrammar_symbols,        ArrayList<graphgrammar_Symbol> graphgrammar_symbols    ) {
        this.name = name;
        this.graphgrammar_symbols = graphgrammar_symbols;
        this.graphgrammar_symbols = graphgrammar_symbols;
        this.graphgrammar_symbols = graphgrammar_symbols;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<graphgrammar_Symbol> getGraphgrammar_symbols() {
        return graphgrammar_symbols;
    }

    public void addGraphgrammar_symbol(Graphgrammar_symbol graphgrammar_symbol) {
        this.graphgrammar_symbols.add(graphgrammar_symbol);
    }
    public List<graphgrammar_Symbol> getGraphgrammar_symbols() {
        return graphgrammar_symbols;
    }

    public void addGraphgrammar_symbol(Graphgrammar_symbol graphgrammar_symbol) {
        this.graphgrammar_symbols.add(graphgrammar_symbol);
    }
    public List<graphgrammar_Symbol> getGraphgrammar_symbols() {
        return graphgrammar_symbols;
    }

    public void addGraphgrammar_symbol(Graphgrammar_symbol graphgrammar_symbol) {
        this.graphgrammar_symbols.add(graphgrammar_symbol);
    }
    public graphgrammar_Symbol getGraphgrammar_symbol() {
        return graphgrammar_symbol;
    }

    public void setGraphgrammar_symbol(graphgrammar_Symbol graphgrammar_symbol) {
        this.graphgrammar_symbol = graphgrammar_symbol;
    }

}