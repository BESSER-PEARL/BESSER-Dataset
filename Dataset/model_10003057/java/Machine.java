





import java.util.List;
import java.util.ArrayList;

public class Machine  {






    private List<Memory_Interface> memory_interfaces;




    private List<Card> cards;




    private List<Processor> processors;


    public Machine(
    ) {
        this.memory_interfaces = new ArrayList<>();
        this.cards = new ArrayList<>();
        this.processors = new ArrayList<>();
    }

    public Machine(
        ArrayList<Memory_Interface> memory_interfaces,        ArrayList<Card> cards,        ArrayList<Processor> processors    ) {
        this.memory_interfaces = memory_interfaces;
        this.cards = cards;
        this.processors = processors;
    }


    public List<Memory_Interface> getMemory_interfaces() {
        return memory_interfaces;
    }

    public void addMemory_interface(Memory_interface memory_interface) {
        this.memory_interfaces.add(memory_interface);
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