import React, { useState, useRef, useEffect } from 'react';
import './Estilo/Estilo.css';
import Logo from './Imagens/Logo.png';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faPaperPlane, faBars, faPencilSquare, faUserCircle, faCaretDown } from '@fortawesome/free-solid-svg-icons';
import { Tooltip } from 'react-tooltip';
import Logo_Puc from './Imagens/puc.png';
import Devs from './Imagens/Devs.png';

const App = () => {
    const [text, setText] = useState('');
    const [messages, setMessages] = useState([]);
    const [sidebarOpen, setSidebarOpen] = useState(true);
    const messagesEndRef = useRef(null);

    const links = [
        { text: 'Delegacia Eletrônica SP', url: 'https://www.delegaciaeletronica.policiacivil.sp.gov.br' },
        { text: 'Disque Denúncia', url: 'https://www.disquedenuncia.org.br' },
        { text: 'Polícia Federal', url: 'http://www.pf.gov.br/servicos-pf/sisden' },
        { text: 'SaferNet Brasil', url: 'https://new.safernet.org.br/denuncie' },
        { text: 'Disque 100', url: 'https://www.gov.br/mdh/pt-br/ondh/disque-100' },
        { text: 'MPF - Sala de Atendimento ao Cidadão', url: 'https://www.mpf.mp.br/para-o-cidadao/sac' },
        { text: 'Procon-SP', url: 'https://www.procon.sp.gov.br' },
        { text: 'MPT - Denúncia Online', url: 'https://www.prtsp.mpt.mp.br/servicos/denuncias' }
    ];

    const handleChange = (e) => {
        setText(e.target.value);
    };

    const handleSubmit = () => {
        if (text.trim()) {
            setMessages([...messages, text]);
            setText('');
        }
    };

    const handleEnterPress = (e) => {
        if (e.key === 'Enter' && !e.shiftKey) {
            e.preventDefault();
            handleSubmit();
        }
    };

    const handleRegister = () => {
        console.log("Cadastro Realizado");
    };

    const handleClearChat = () => {
        setMessages([]);
    };

    const toggleSidebar = () => {
        setSidebarOpen(!sidebarOpen);
    };

    useEffect(() => {
        messagesEndRef.current.scrollTop = messagesEndRef.current.scrollHeight;

    }, [messages]);


    return (
        <div className="App">
            <Tooltip id="tooltip" className="tooltip" />

            <img className="logo" src={Logo} alt="Logo" />

            <button className="Botao_Novo_Chat_2" onClick={handleClearChat} data-tooltip-id="tooltip" data-tooltip-content="Novo Chat">
                <FontAwesomeIcon icon={faPencilSquare} style={{ fontSize: '29px' }} />
            </button>

            <button className="Logo_Info" onClick={handleClearChat} data-tooltip-id="tooltip" data-tooltip-content="Novo Chat">
                <FontAwesomeIcon icon={faCaretDown} style={{ fontSize: '29px' }} />
            </button>


            <button className="Botao_Menu" onClick={toggleSidebar} data-tooltip-id="tooltip" data-tooltip-content="Abrir barra lateral">
                <FontAwesomeIcon icon={faBars} style={{ fontSize: '25px' }} />
            </button>

            <div className={`Sidebar ${sidebarOpen ? 'open' : ''}`}>

                <button className="Botao_Menu" onClick={toggleSidebar} data-tooltip-id="tooltip" data-tooltip-content="Fechar barra lateral">
                    <FontAwesomeIcon icon={faBars} style={{ fontSize: '25px' }} />
                </button>

                <button className="Botao_Novo_Chat" onClick={handleClearChat} data-tooltip-id="tooltip" data-tooltip-content="Novo Chat">
                    <FontAwesomeIcon icon={faPencilSquare} style={{ fontSize: '29px' }} />
                </button>

                <h3 className='Titulo_1'>Faça a Diferença: Denuncie Online e Combata a Injustiça!</h3>
                <ul className='Links'>
                    {links.map((link, index) => (
                        <li key={index}>
                            <a href={link.url} target="_blank" rel="noopener noreferrer">{link.text}</a>
                        </li>
                    ))}
                </ul>

                <img className='Logo_Puc' src={Logo_Puc} alt='Logo' />

           
       
           
           
            </div>

            <div className="Retangulo">
                <div className="Mensagens" ref={messagesEndRef}>
                    {messages.map((msg, index) => (
                        <div key={index} className="Mensagem">
                            {msg}
                        </div>
                    ))}
                </div>

                <textarea
                    className="Caixa-texto"
                    value={text}
                    onChange={handleChange}
                    onKeyDown={handleEnterPress}
                    placeholder="Mensagem JustAI"
                />

                <button className="Botao_Enviar" onClick={handleSubmit}>
                    <FontAwesomeIcon icon={faPaperPlane} />
                </button>

            </div>

            <button className='Users' onClick={handleRegister} data-tooltip-id="tooltip" data-tooltip-content={"Cadastre-se"}>
                <FontAwesomeIcon icon={faUserCircle} style={{ fontSize: '30px' }} className='UsersIcon' /></button>

            
                <img className='Devs' src={Devs} alt='Devs '/>



        </div>
    );
};

export default App;
