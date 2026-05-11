





import java.util.List;
import java.util.ArrayList;

public class graphgrammar_SymbolSymbolsPair  {






    private List<graphgrammar_Symbol> graphgrammar_symbols;




    private graphgrammar_VertexToSymbolSymbolsPairMap graphgrammar_vertextosymbolsymbolspairmap;




    private graphgrammar_Symbol graphgrammar_symbol;


    public graphgrammar_SymbolSymbolsPair(
    ) {
        this.graphgrammar_symbols = new ArrayList<>();
    }

    public graphgrammar_SymbolSymbolsPair(
        ArrayList<graphgrammar_Symbol> graphgrammar_symbols    ) {
        this.graphgrammar_symbols = graphgrammar_symbols;
    }


    public List<graphgrammar_Symbol> getGraphgrammar_symbols() {
        return graphgrammar_symbols;
    }

    public void addGraphgrammar_symbol(Graphgrammar_symbol graphgrammar_symbol) {
        this.graphgrammar_symbols.add(graphgrammar_symbol);
    }
    public graphgrammar_VertexToSymbolSymbolsPairMap getGraphgrammar_vertextosymbolsymbolspairmap() {
        return graphgrammar_vertextosymbolsymbolspairmap;
    }

    public void setGraphgrammar_vertextosymbolsymbolspairmap(graphgrammar_VertexToSymbolSymbolsPairMap graphgrammar_vertextosymbolsymbolspairmap) {
        this.graphgrammar_vertextosymbolsymbolspairmap = graphgrammar_vertextosymbolsymbolspairmap;
    }
    public graphgrammar_Symbol getGraphgrammar_symbol() {
        return graphgrammar_symbol;
    }

    public void setGraphgrammar_symbol(graphgrammar_Symbol graphgrammar_symbol) {
        this.graphgrammar_symbol = graphgrammar_symbol;
    }

}