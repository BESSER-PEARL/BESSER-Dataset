





import java.util.List;
import java.util.ArrayList;

public class yyf_NamedElement  {

    private String name;





    private List<yyf_Alias> yyf_aliass;




    private List<yyf_Bar> yyf_bars;


    public yyf_NamedElement(
        String name    ) {
        this.name = name;
        this.yyf_aliass = new ArrayList<>();
        this.yyf_bars = new ArrayList<>();
    }

    public yyf_NamedElement(
        String name        ArrayList<yyf_Alias> yyf_aliass,        ArrayList<yyf_Bar> yyf_bars    ) {
        this.name = name;
        this.yyf_aliass = yyf_aliass;
        this.yyf_bars = yyf_bars;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<yyf_Alias> getYyf_aliass() {
        return yyf_aliass;
    }

    public void addYyf_alias(Yyf_alias yyf_alias) {
        this.yyf_aliass.add(yyf_alias);
    }
    public List<yyf_Bar> getYyf_bars() {
        return yyf_bars;
    }

    public void addYyf_bar(Yyf_bar yyf_bar) {
        this.yyf_bars.add(yyf_bar);
    }

}