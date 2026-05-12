





import java.util.List;
import java.util.ArrayList;

public class Machine  {






    private List<Card> cards;




    private List<Processor> processors;


    public Machine(
    ) {
        this.cards = new ArrayList<>();
        this.processors = new ArrayList<>();
    }

    public Machine(
        ArrayList<Card> cards,        ArrayList<Processor> processors    ) {
        this.cards = cards;
        this.processors = processors;
    }


    public List<Card> getCards() {
        return cards;
    }

    public void addCard(Card card) {
        this.cards.add(card);
    }
    public List<Processor> getProcessors() {
        return processors;
    }

    public void addProcessor(Processor processor) {
        this.processors.add(processor);
    }

}