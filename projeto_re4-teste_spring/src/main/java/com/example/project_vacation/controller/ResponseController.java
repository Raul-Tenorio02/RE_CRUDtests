package com.example.project_vacation.controller;

import com.example.project_vacation.model.Response;
import com.example.project_vacation.repository.ResponseRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.*;

@Controller
@RequestMapping("/responses")
public class ResponseController {

    @Autowired
    private ResponseRepository responseRepository;

    @GetMapping
    public String listResponse(Model model) {
        model.addAttribute("responses", responseRepository.findAll());
        return "responses";
    }

    @GetMapping("/form")
    public String showFormulary(Model model) {
        model.addAttribute("response", new Response());
        return "form";
    }

    @PostMapping
    public String saveResponse(@ModelAttribute Response response) {
        responseRepository.save(response);
        return "redirect:/responses";
    }

    @GetMapping("/delete/{id}")
    public String deleteResponse(@PathVariable Long id) {
        responseRepository.deleteById(id);
        return "redirect:/responses";
    }
}